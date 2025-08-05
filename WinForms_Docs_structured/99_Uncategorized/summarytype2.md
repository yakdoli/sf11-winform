---
title: summarytype2.md
original_path: WinForms_Docs/99_Uncategorized/summarytype2.md
created_at: 2025-08-05
---








  









## SummaryType {#summarytype style="tab-stops: 0pt"}

SummaryType determines the type of field summary such as count, sum, average, etc. It is an enumerator that should be defined in the *PivotComputationInfo* class. It contains the following types for performing calculations.

Table 9: Summary Type Table

+-----------------------------------+-------------------------------------------------------------------------------------+
|                                   |                                                                                     |
|                                   |                                                                                     |
| Summary Type                      | Description                                                                         |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DoubleTotalSum                    | Computes the sum of double or integer values.                                       |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DoubleAverage                     | Computes the simple average of double or integer values.                            |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DoubleMaximum                     | Computes the maximum of double or integer values.                                   |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DoubleMinimum                     | Computes the minimum of double or integer values.                                   |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DoubleStandardDeviation           | Computes the standard deviation of double or integer values.                        |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DoubleVariance                    | Computes the variance of double or integer values.                                  |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Count                             | Computes the count of double or integer values.                                     |
+-----------------------------------+-------------------------------------------------------------------------------------+
| DecimalTotalSum                   | Computes the sum of decimal values.                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------+
| IntTotalSum                       | Computes the sum of integer values.                                                 |
+-----------------------------------+-------------------------------------------------------------------------------------+
| Custom                            | Specifies that you are using a custom SummaryBase object to define the calculation. |
+-----------------------------------+-------------------------------------------------------------------------------------+

[]{#related-topics}

