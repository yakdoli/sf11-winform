---
title: renamereport.md
original_path: WinForms_Docs/99_Uncategorized/renamereport.md
created_at: 2025-08-05
---








  









### RenameReport {#renamereport style="tab-stops: 0pt"}

A report in the report collection of OlapDataManager can be renamed by invoking RenameReport method with arguments such as, index of the report and new name for the report or with old name and new name of the report. The following code snippet will illustrate this:

+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]                                                    ]**                                                                                                          |
|                                                                                                                                                                                                               |
| []                                                                                                                                                                        |
|                                                                                                                                                                                                               |
| [olapDataManager.RenameReport(2, [\"SalesAnalysisOn2003\"]);]                                                                                     |
|                                                                                                                                                                                                               |
| [olapDataManager.RenameReport([\"RevenueAnalysis\"], [\"RevenueAnalysisOn2003\"]);][] |
+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                                                                                                             |
|                                                                                                                                                                                                              |
| [       ]                                                                                                                                                                |
|                                                                                                                                                                                                              |
| [olapDataManager.RenameReport(2, [\"SalesAnalysisOn2003\"])]                                                                                     |
|                                                                                                                                                                                                              |
| [olapDataManager.RenameReport([\"RevenueAnalysis\"], [\"RevenueAnalysisOn2003\"])][] |
+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

 

[]{#related-topics}

