---
title: normaldistribution1.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\normaldistribution1.md
created_at: 2025-07-03
---






#### Normal Distribution {#normal-distribution style="tab-stops: 0pt"}

 

This formula yields the value of the standard normal cumulative distribution. Normal distributions are symmetric and have bell-shaped density curves with a single peak. Two factors, the mean (*[μ]*) and the standard deviation ([σ]), come into place when we speak of normal distribution. The mean indicates the peak of the density curve and the standard deviation indicates the spread of the bell curve.

 

The normal density function is given by,

 

{border="0"}

 

 

{border="0"}

Figure 345: Normal Density Function

 

 

Different values of *[μ][ ]*and [σ] yield different normal density curves and hence different normal distributions.  All normal density curves satisfy the following property which is often referred to as the*[ ]*Empirical Rule.

 

[·      ]68% of the observations fall within 1 standard deviation of the mean, that is, between *[μ]* - [σ] and *[μ]* + [σ].

[·      ]95% of the observations fall within 2 standard deviations of the mean, that is, between *[μ]* - 2[σ] and *[μ]* + 2[σ].

[·      ]99.7% of the observations fall within 3 standard deviations of the mean, that is, between *[μ]* - 3[σ] and *[μ]* + 3[σ].

 

Thus, for a normal distribution, almost all values lie within three standard deviations of the mean.

 

Using the Formula

 

NormalDistribution is calculated using the **Statistics.UtilityFunctions** class. The following table describes this formula\'s parameters and its values.

 


  -------------------- ----------------------------------------------------------- -----------------------------------------------------------------------------
  Method Name          Parameters                                                  Return Value
  NormalDistribution   zValue: The value for which the distribution is required.   A double that represents the standard normal cumulative distribution value.
  -------------------- ----------------------------------------------------------- -----------------------------------------------------------------------------


 

Example

 

Here is a code snippet that shows a sample usage.

 

+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                         |
|                                                                                                                                                                        |
| []                                                                                                                                               |
|                                                                                                                                                                        |
| [using Syncfusion.Windows.Forms.Chart.Statistics;]                                                                   |
|                                                                                                                                                                        |
| [double][ x = Statistics.UtilityFunctions.NormalDistribution( p );] |
+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                    |
|                                                                                                                                                                       |
| []                                                                                                                                              |
|                                                                                                                                                                       |
| [Imports Syncfusion.Windows.Forms.Chart.Statistics]                                                                 |
|                                                                                                                                                                       |
| [double][ x = Statistics.UtilityFunctions.NormalDistribution( p )] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

[]{#p244} 

[]{#related-topics}

