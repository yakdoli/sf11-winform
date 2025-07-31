---
title: summarytype.md
original_path: c:/workspace/sf11-winform/WinForms_Docs\99_Uncategorized\summarytype.md
created_at: 2025-07-03
---








  









### SummaryType {#summarytype style="tab-stops: 0pt"}

 

**SummaryType** determines the type of field Summary which may be a count or sum or average etc. It is an enumerator which should be defined in **PivotComputationInfo** and it contains the following types for performing calculations.

 


  Type                      Description
  ------------------------- -------------------------------------------------------------------------------------
  DoubleTotalSum            Computes the sum of double or integer values.
  DoubleAverage             Computes the simple average of double or integer values.
  DoubleMaximum             Computes the maximum of double or integer values.
  DoubleMinimum             Computes the minimum of double or integer values.
  DoubleStandardDeviation   Computes the standard deviation of double or integer values.
  DoubleVariance            Computes the variance of double or integer values.
  Count                     Computes the count of double or integer values.
  DecimalTotalSum           Computes the sum of decimal values.
  IntTotalSum               Computes the sum of integer values.
  Custom                    Specifies that you are using a custom SummaryBase object to define the calculation.


 

[]{#related-topics}

