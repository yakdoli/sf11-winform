---
title: ftest1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\ftest1.md
created_at: 2025-07-03
---






#### F-Test {#f-test style="tab-stops: 0pt"}

 

The **F-Test** is a statistical test, which is carried out to find out whether two series have the same standard deviation with the specified confidence level. It is achieved by comparing the variances of the series values and thereby comparing their standard deviations. Here, the null hypothesis is that the two variances are equal. All hypothesis testing is done under the assumption that the null hypothesis is **true**.

 

Steps to perform F-Test

 

1.   Calculate the variances of both the series.

2.   Calculate F Ratio as given below.

 

***F Value*** *= firstSeriesVariance / secondSeriesVariance.*

 

F-Test can be easily performed by using the **FTest** method of **BasicStatisticalFormulas** class that returns the results as a type of **FTestResult**. The FTestResult is a class implemented to save the F test result as **FValue** and other computation results such as series means, series variances, FRatio and FCriticalValue of the test. Below is a detailed table for the FTest method. 

 


+-----------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------+
| Method Name           | Parameters                                                                                      | Returns                                   |
+-----------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------+
| FTest                 | 1\. **Probability**: Probability that gives the confidence level.                               | An FTestResult has the following members: |
|                       |                                                                                                 |                                           |
|                       | 2\. **FirstInputSeries**: Type of ChartSeries object that represents the first group of data.   | FirstSeriesMean                           |
|                       |                                                                                                 |                                           |
|                       | 3\. **SecondInputSeries**: Type of ChartSeries object that represents the second group of data. | SecondSeriesMean                          |
|                       |                                                                                                 |                                           |
|                       |                                                                                                 | FirstSeriesVariance                       |
|                       |                                                                                                 |                                           |
|                       |                                                                                                 | SecondSeriesVariance                      |
|                       |                                                                                                 |                                           |
|                       |                                                                                                 | FValue                                    |
|                       |                                                                                                 |                                           |
|                       |                                                                                                 | ProbabilityFOneTail                       |
|                       |                                                                                                 |                                           |
|                       |                                                                                                 | FCriticalValueOneTail                     |
+-----------------------+-------------------------------------------------------------------------------------------------+-------------------------------------------+


 

Example

 

Here is a code snippet that shows a sample usage.

 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                   |
|                                                                                                                                                                                  |
| []                                                                                                                                                         |
|                                                                                                                                                                                  |
| [FTestResult ttr = Syncfusion.Windows.Forms.Chart.Statistics.BasicStatisticalFormulas.FTest(confidenceLevel,series1,series2);] |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                               |
|                                                                                                                                                                                                                                                                                                                                                  |
| []                                                                                                                                                                                                                                                                                                                         |
|                                                                                                                                                                                                                                                                                                                                                  |
| [Dim][ ttr ][As][ FTestResult = Syncfusion.Windows.Forms.Chart.Statistics.BasicStatisticalFormulas.FTest(confidenceLevel,series1,series2)] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 


{border="0"}Note: For further details, refer to this Browser Sample:


 

[\[Installed drive\]:\\Documents and Settings\\\[User name\]\\My Documents\\Syncfusion\\EssentialStudio\\\[Installed version\]\\Windows\\Chart.Windows\\Samples\\2.0\\Statistical Analysis\\Chart Statistical Formulas]{.UGHyperlink}

 

[]{#p221} 

[]{#related-topics}

