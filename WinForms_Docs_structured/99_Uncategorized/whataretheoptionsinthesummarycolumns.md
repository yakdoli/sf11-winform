---
title: whataretheoptionsinthesummarycolumns.md
original_path: WinForms_Docs/99_Uncategorized/whataretheoptionsinthesummarycolumns.md
created_at: 2025-08-05
---






#### What are the options in the summary columns? {#what-are-the-options-in-the-summary-columns style="tab-stops: 0pt"}

[] 

The options in the summary columns are illustrated using the below code.

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[C#\]]**                                                                    |
|                                                                                                                                   |
| []                                                                            |
|                                                                                                                                   |
| [// Disabling the change of summary value during the filter criteria.]          |
|                                                                                                                                   |
| [// sd is GridSummaryColumnDescriptor ]                                         |
|                                                                                                                                   |
| [// This ignores filtering of the grid. So, the summary value doesn\'t change.] |
|                                                                                                                                   |
| [sd.IgnoreRecordFilterCriteria=[true];]                                  |
+-----------------------------------------------------------------------------------------------------------------------------------+

[] 

+-----------------------------------------------------------------------------------------------------------------------------------+
| **[\[VB\]]**                                                                    |
|                                                                                                                                   |
| []                                                                            |
|                                                                                                                                   |
| [\'Disabling the change of summary value during the filter criteria.]           |
|                                                                                                                                   |
| [\' sd is GridSummaryColumnDescriptor ]                                         |
|                                                                                                                                   |
| [\' This ignores filtering of the grid. So, the summary value doesn\'t change.] |
|                                                                                                                                   |
| [sd.IgnoreRecordFilterCriteria=[True]]                                   |
+-----------------------------------------------------------------------------------------------------------------------------------+

 

[]{#p672} 

 

[]{#related-topics}

