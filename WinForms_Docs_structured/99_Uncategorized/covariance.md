---
title: covariance.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\covariance.md
created_at: 2025-07-03
---






#### Covariance {#covariance style="tab-stops: 0pt"}

[] 

**Covariance** is a statistical formula that measures the extent to which the y values of two series vary together. It is basically used to measure the fluctuations between two quantities. For a given pairs of series y values, the covariance can be calculated by taking their differences from their mean values and multiplying these differences together. That is,

[] 

*[Cov(x,y) = ][Σ][{\[ x-][Σ][(x) \]\[ y-][Σ][(y) \]}]*

[] 

If this product is **positive**, then the values would be varying in the same direction; if it is **negative**, then the values would be varying in opposite directions. If the product is **zero**, then we can conclude that there is no linear relationship between the series values. The above formula can be simplified as below.

[] 

*[Cov(x,y) = ][Σ][{xy} - ][Σ][{x}][Σ][{y}]*

[] 

Using the Formula

[] 

The Covariance can easily be calculated by using the **Covariance** method available with the **BasicStatisticalFormulas** class. The following table describes the details of this method.

[] 


+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
|                       |                                                                                                                                                                                       |                                                                                         |
|                       |                                                                                                                                                                                       |                                                                                         |
| Method Name           | Parameters                                                                                                                                                                            | Return Value                                                                            |
+=======================+=======================================================================================================================================================================================+=========================================================================================+
| Covariance            | 1\. **FirstInputSeriesName**: A ChartSeries object that stores the first group\'s data.                                                                                               | A **double** value that represents the covariance value between the two groups of data. |
|                       |                                                                                                                                                                                       |                                                                                         |
|                       | 2\. **SecondInputSeriesName**: A ChartSeries object that stores the second group\'s data. An exception will be raised if the input series do not have the same number of data points. |                                                                                         |
+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+


[] 

Example

[] 

Here is the code snippet that demonstrates the usage of this method.

[] 

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                                              |
|                                                                                                                                                                                             |
| **[]**                                                                                                                                    |
|                                                                                                                                                                                             |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                                        |
|                                                                                                                                                                                             |
| [\...\...\...\...]                                                                                                                        |
|                                                                                                                                                                                             |
| [double][ Covariance1= Statistics.BasicStatisticalFormulas.Covariance(series1,series2);] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                  |
|                                                                                                                                                                                     |
| **[]**                                                                                                                            |
|                                                                                                                                                                                     |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                               |
|                                                                                                                                                                                     |
| [\...\...\...\....]                                                                                                               |
|                                                                                                                                                                                     |
| [Dim][ Covariance1 ][As Double] |
|                                                                                                                                                                                     |
| [Covariance1=BasicStatisticalFormulas.Covariance (series,series1)]                                                                |
+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


{border="0"}Note: For further details, refer the following Browser Sample:


[] 

\[Install Location\]\\Syncfusion\\EssentialStudio\\\[***Installed version***\]\\Web\\chart.web\\Samples\\3.5\\Statistics\\ChartStatisticalFormulas

[]{#p220} 

[]{#related-topics}

