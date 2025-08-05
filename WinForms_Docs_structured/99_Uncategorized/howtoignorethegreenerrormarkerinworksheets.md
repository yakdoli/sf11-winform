---
title: howtoignorethegreenerrormarkerinworksheets.md
original_path: WinForms_Docs/99_Uncategorized/howtoignorethegreenerrormarkerinworksheets.md
created_at: 2025-08-05
---








  









### How to ignore the green error marker in worksheets? {#how-to-ignore-the-green-error-marker-in-worksheets style="tab-stops: 0pt"}

 

You can ignore the error marker that appears in cells, when there exists data that are of different formats. This can be done by using the ExcelIgnoreError enumerator that provides various options to ignore the error marker.

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                                                       |
|                                                                                                                                                        |
| []                                                                                                                 |
|                                                                                                                                                        |
| [// Ignore Error Options.]                                                                           |
|                                                                                                                                                        |
| [sheet.Range\[[\"B3\"]\].IgnoreErrorOptions = [ExcelIgnoreError].All;] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB.NET\]]**                                                                                                |
|                                                                                                                                                     |
| []                                                                                                              |
|                                                                                                                                                     |
| [\' Ignore Error Options.]                                                                        |
|                                                                                                                                                     |
| [sheet.Range([\"B3\")].IgnoreErrorOptions = [ExcelIgnoreError].All] |
+-----------------------------------------------------------------------------------------------------------------------------------------------------+

[] 

{border="0"}

Figure 163: To ignore error[]

[] 

[]{#related-topics}

