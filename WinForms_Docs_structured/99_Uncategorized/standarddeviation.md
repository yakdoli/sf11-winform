---
title: standarddeviation.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\standarddeviation.md
created_at: 2025-07-03
---






#### Standard Deviation {#standard-deviation style="tab-stops: 0pt"}

[] 

**StandardDeviation** is the statistical formula that is basically used to measure the variability. That is, it can be used to measure how spread out your data is. It can be defined as the square root of the variance where a variance is the average of the squared differences between the data points and the mean. In other words, it is named as the \'root-mean-square\' of the data values.

It can be used to check how tightly the data values are clustered around the mean. If the data points are close to the mean, then the standard deviation will be small or if the points are far from the mean, then the standard deviation is large or if all the data values are equal, then the standard deviation is **zero**.

The Standard Deviation can be calculated for any series by using the **StandardDeviation** method of **BasicStatisticalFormulas** class. Below is the detailed description of this method.

[] 


+-----------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
|                       |                                                                                                              |                                                                               |
|                       |                                                                                                              |                                                                               |
| Method Name           | Parameters                                                                                                   | Return Value                                                                  |
+-----------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
| StandardDeviation     | 1.   **InputSeries**: A ChartSeries type object for on whose Y values this formula should be applied.        | A **double** that represents the standard deviation within the group of data. |
|                       |                                                                                                              |                                                                               |
|                       | 2.   **SampleVariance**: true if the data is a sample of a population, false if it is the entire population. |                                                                               |
+-----------------------+--------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+


[] 

Example

[] 

Here is a code snippet that shows a sample usage.

[  ]

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                        |
|                                                                                                                                                                                       |
| **[]**                                                                                                                              |
|                                                                                                                                                                                       |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                  |
|                                                                                                                                                                                       |
| [\...\...\...\...]                                                                                                                  |
|                                                                                                                                                                                       |
| [double][ Deviation1 = BasicStatisticalFormulas.StandartDeviation(series1,false);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                 |
|                                                                                                                                                                                    |
| **[]**                                                                                                                           |
|                                                                                                                                                                                    |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                              |
|                                                                                                                                                                                    |
| [\...\...\...\....]                                                                                                              |
|                                                                                                                                                                                    |
| [Dim][ Deviation1 ][As Double] |
|                                                                                                                                                                                    |
| [Deviation1 = BasicStatisticalFormulas. StandartDeviation  (series1,false)]                                                      |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: For further details, refer the following Browser Sample:


[] 

\[Install Location\]\\Syncfusion\\EssentialStudio\\\[***Installed version***\]\\Web\\chart.web\\Samples\\3.5\\Statistics\\ChartStatisticalFormulas

[]{#p224} 

[]{#related-topics}

