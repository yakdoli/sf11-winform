---
title: mean.md
original_path: WinForms_Docs/99_Uncategorized/mean.md
created_at: 2025-08-05
---






#### Mean {#mean style="tab-stops: 0pt"}

[] 

**Mean** is statistical formula that returns the arithmetic average of series y values where the arithmetic average is the sum of all y values of a series divided by the total number of y values present in that series. The arithmetic mean can be calculated for any chart series by using **Mean** method of the **BasicStatisticalFormulas** class. Below table shows the method details.

[] 


  ------------- --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------
  Method Name   Parameter                                                                               Return value
  Mean          **InputSeries**: A ChartSeries type object for whose y values an average is required.   A **double** that represents the average of all the  y values in the given series.
  ------------- --------------------------------------------------------------------------------------- ------------------------------------------------------------------------------------


[] 

Example

[] 

Here is a code snippet that shows a sample usage.

[] 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                                               |
|                                                                                                                                                                        |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                   |
|                                                                                                                                                                        |
| [\...\...\...\...]                                                                                                   |
|                                                                                                                                                                        |
| [double][ calculatedMean = BasicStatisticalFormulas.Mean(series1);] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                                     |
|                                                                                                                                                                                        |
| []                                                                                                                                                               |
|                                                                                                                                                                                        |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                                  |
|                                                                                                                                                                                        |
| [\...\...\...\....]                                                                                                                  |
|                                                                                                                                                                                        |
| [Dim][ calculatedMean ][As Double] |
|                                                                                                                                                                                        |
| [calculatedMean = BasicStatisticalFormulas.Mean(series1)]                                                                            |
+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 


[{border="0"}]Note: For further details, refer the following Browser Sample:


[] 

\[Install Location\]\\Syncfusion\\EssentialStudio\\\[***Installed version***\]\\Web\\chart.web\\Samples\\3.5\\Statistics\\ChartStatisticalFormulas

[]{#p222} 

[]{#related-topics}

