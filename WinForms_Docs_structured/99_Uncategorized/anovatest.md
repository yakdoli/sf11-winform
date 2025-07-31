---
title: anovatest.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\anovatest.md
created_at: 2025-07-03
---






#### Anova Test {#anova-test style="tab-stops: 0pt"}

[] 

**Anova** stands for **Analysis Of Variance**. It is a technique to test the hypothesis that the means among two or more groups of data are equal and thereby, testing the differences between their variances, under the assumption that the sampled groups are normally distributed.

 

The test actually compares the variation between the groups with the variation within the groups and produces the results based on the values of these variations. If the between variation is larger than the within variation, the means of the groups will not be equal. If both these variations are of approximately the same size, then there will not be any significant difference between the means.

[] 

Steps to perform an Anova test

**[]** 

The null hypothesis is that there is no difference between the means and the alternative hypothesis is that at least one mean is different.

 

The following assumptions must be satisfied before performing the test.

[] 

[·      ]The groups from which the samples were obtained must be normally distributed.

[·      ]The groups are sampled randomly.

[·      ]The samples must be independent.

[·      ]The variances of the groups must be equal.

[·      ]The null hypothesis.

[] 

[] 

1.   Calculate the **Sum of Squares** for total, between and within variations.

[] 

**[Total Variation]**

[] 

[{border="0"}][]

[] 

**[]** 

**[Between Variation]**

[] 

[{border="0"}][]

[] 

Where:

y is the individual y points of the series,

r is the number of series present,

N is the total number of y points for all the series and

n is the number of y points in each series.

[] 

Within Variation

*[]* 

SSwithin = SStotal - SSamong

[] 

2.   Using the above quantities, calculate the degrees of freedom(df) for these variations.

[] 

Between Variation

*[]* 

dfamong = r-1

*[]* 

Within Variation      

*[]* 

dfwithin = N-r

*[]* 

Where,

r is the number of series present and

N is the total number of Y points for all the series.

*[]* 

3.   As the next step, calculate the Mean Squares of these variations. The mean square for a variation can be calculated simply by dividing its sum of square by its degrees of freedom.

[] 

**[Between Variation]**

**[]** 

**[{border="0"}][]**

*[]* 

**[Within Variation]**[    ]

[] 

[{border="0"}][]

[] 

4.   Finally, calculate **F Ratio** as below and get the **F Critical Value**.

[] 

[{border="0"}][]

*[]* 

5.   Make your decision as below.

[] 

[·      ]If the *between* variance is smaller than the *within* variance, then the *means* are really close to each other and you will fail to reject the null hypothesis.

[·      ]If the F ratio is greater than the F critical value, then  the decision will be to reject the null hypothesis and thereby conclude that at least one of the means is different.

[] 

APIs Used

[] 

Essential Chart provides support to perform Anova Test by implementing a method named Anova in the **BasicStatisticalFormulas** class. This method does the above described calculations and returns the test results as an instance of **AnovaResult** class. The AnovaResult is a class implemented to store the anova test results such as  sum of squares, degrees of freedom and mean squares for different variations and also stores the **FRatio** and **FCriticalValue** of the test. Below is a detailed table for the Anova method.

[] 


+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Method Name           | Parameters                                                                                                                                                                        | Return Values                                                         |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+
| Anova                 | 1\. Probability: the alpha value (probability).                                                                                                                                   | An Anova has the following members:                                   |
|                       |                                                                                                                                                                                   |                                                                       |
|                       | 2\. InputSeries: references to two or more input series. Each series must exist in the series collection at the time of the method call, and have the same number of data points. | [·      ]DegreeOfFreedomBetweenGroups    |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]DegreeOfFreedomTotal            |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]DegreeOfFreedomWithinGroups     |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]FCriticalValue                  |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]FRatio                          |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]MeanSquareVarianceBetweenGroups |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]MeanSquareVarianceWithinGroups  |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]SumOfSquaresBetweenGroups       |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]SumOfSquaresTotal               |
|                       |                                                                                                                                                                                   |                                                                       |
|                       |                                                                                                                                                                                   | [·      ]SumOfSquaresWithinGroups        |
+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------+


[] 

Here is a sample code snippet to simulate an Anova test.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                            |
|                                                                                                                                                           |
| []                                                                                                                                  |
|                                                                                                                                                           |
| [AnovaResult ar = BasicStatisticalFormulas.Anova(confidenceLevel,]                                      |
|                                                                                                                                                           |
| [new][ ChartSeries\[\]{ series1, series2, series3} );] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                                                                                                                                                                                                                                                                          |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| []                                                                                                                                                                                                                                                                                                                                                                                                                    |
|                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Dim][ ar ][As][ AnovaResult = BasicStatisticalFormulas.Anova(confidenceLevel, ][New][ ChartSeries(){ series1, series2, series3})] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

The following image displays the results of an ANOVA test.

[] 

{border="0"}

**[]** 

Figure 307: Anova Test

[]{#p218} 

[]{#related-topics}

